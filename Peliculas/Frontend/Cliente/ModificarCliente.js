fetch(`http://localhost:3000/getUsuarioEnSesion`, {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
    }
})
    .then(res => res.json())
    .catch(err => {
        console.error('Error:', err)
        alert("Ocurrio un error")
    })
    .then(response => {
        console.log(response)
        usuarioEnSesion = response.data
        document.getElementById("ModificarCliente-nombre").value = usuarioEnSesion.nombre
        document.getElementById("ModificarCliente-apellido").value = usuarioEnSesion.apellido
        document.getElementById("ModificarCliente-nombre_usuario").value = usuarioEnSesion.nombre_usuario
        document.getElementById("ModificarCliente-password").value = usuarioEnSesion.contrasenia
    })

function ModificarCliente() {
        var nombre = document.getElementById("ModificarCliente-nombre").value;
        var apellido = document.getElementById("ModificarCliente-apellido").value;
        var nombre_usuario = document.getElementById("ModificarCliente-nombre_usuario").value;
        var contrasenia = document.getElementById("ModificarCliente-password").value;
    
        var objeto = {
            'nombre': nombre,
            'apellido': apellido,
            'nombre_usuario': nombre_usuario,
            'contrasenia': contrasenia,
            'tipo': 1
        };
        
        console.log(objeto);
    
        fetch('http://localhost:3000/modificarCliente', {
            method: 'POST',
            body: JSON.stringify(objeto),
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
            }
        }).then(res => res.json())
            .catch(err => {
                console.error('Error:', err);
                alert("Ocurrió un error");
            }).then(response => {
                console.log(response);
                if (response.status == 400) {
                    alert("Ocurrió un error");
                } else {
                    alert("Usuario actualizado!");
                }
            });
 }
    