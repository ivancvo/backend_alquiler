from flask import Blueprint, request, jsonify, render_template
from ..app import  db 
from ..modelos.modelos import Usuario, Vehiculo
from ..modelos.modelos import UsuarioSchema, VehiculoSchema
from werkzeug.utils import secure_filename
import cloudinary
import cloudinary.uploader
import cloudinary.api
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity

admin_blueprint = Blueprint('admin',__name__ )

@admin_blueprint.route('/admin/usuarios')

@jwt_required()

def get_usuarios():
    usuarios = Usuario.query.all()
    esquema = UsuarioSchema(many=True)
    return jsonify(esquema.dump(usuarios))


@admin_blueprint.route('/admin/usuarios/<int:id>', methods=['PUT', 'DELETE'])

@jwt_required()
def actualizar_eliminar_usuario(id):
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({'error': 'Usuario no encontrado'}), 404

    if request.method == 'PUT':
        nueva_data = request.get_json()
        esquema = UsuarioSchema()
        esquema.load(nueva_data, instance=usuario)
        db.session.commit()
        return jsonify({'mensaje': 'Usuario actualizado exitosamente'})

    if request.method == 'DELETE':
        db.session.delete(usuario)
        db.session.commit()
        return jsonify({'mensaje': 'Usuario eliminado exitosamente'})

@admin_blueprint.route('/admin/vehiculos')
@jwt_required()
def get_vehiculos():
    vehiculos = Vehiculo.query.all()
    esquema = VehiculoSchema(many=True)
    return jsonify(esquema.dump(vehiculos))

@admin_blueprint.route('/admin/vehiculos', methods=['POST'])
@jwt_required()
def crear_vehiculo():
    nueva_data = request.form
    # Subir la imagen a Cloudinary
    imagen = request.files['foto']
    resultado = cloudinary.uploader.upload(imagen)
    nueva_data['Foto_Vehiculo'] = resultado['secure_url']

    esquema = VehiculoSchema()
    nuevo_vehiculo = esquema.load(nueva_data)
    db.session.add(nuevo_vehiculo)
    db.session.commit()
    return jsonify({'mensaje': 'Vehículo creado exitosamente!'})

@admin_blueprint.route('/admin/vehiculos/<int:id>', methods=['PUT', 'DELETE'])
@jwt_required()
def actualizar_eliminar_vehiculo(id):
    vehiculo = Vehiculo.query.get(id)
    if not vehiculo:
        return jsonify({'error': 'Vehículo no encontrado'}), 404

    if request.method == 'PUT':
        nueva_data = request.form
        # Si se envía una nueva imagen, actualizar en Cloudinary
        if 'foto' in request.files:
            imagen = request.files['foto']
            resultado = cloudinary.uploader.upload(imagen)
            nueva_data['Foto_Vehiculo'] = resultado['secure_url']

        esquema = VehiculoSchema()
        esquema.load(nueva_data, instance=vehiculo)
        db.session.commit()
        return jsonify({'mensaje': 'Vehículo actualizado exitosamente'})

    if request.method == 'DELETE':
        # Eliminar la imagen de Cloudinary si es necesario
        if vehiculo.Foto_Vehiculo:
            public_id = cloudinary.utils.cloudinary_url(vehiculo.Foto_Vehiculo).split('/')[1]
            cloudinary.uploader.destroy(public_id)

        db.session.delete(vehiculo)
        db.session.commit()
        return jsonify({'mensaje': 'Vehículo eliminado exitosamente'})

