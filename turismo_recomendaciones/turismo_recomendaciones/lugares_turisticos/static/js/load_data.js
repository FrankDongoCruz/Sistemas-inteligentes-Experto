fetch('/lugares-con-calificaciones-json/') // Ruta correcta a tu vista
    .then(response => response.json())
    .then(data => {
        const lugaresContainer = document.getElementById('lugares-container');
        data.forEach(lugar => {
            const lugarHTML = `
                <div class="border border-gray-300 p-6 rounded-lg">
                    <h2 class="text-xl font-bold mb-2">${lugar.nombre}</h2>
                    <img src="${lugar.imagen_url}" alt="${lugar.nombre}" class="mb-4 rounded-lg">
                    <p class="mb-2">Ubicación: ${lugar.ubicacion}</p>
                    <p class="mb-2">Categoría: ${lugar.categoria}</p>
                    <p class="mb-2">Calificación: ${lugar.promedio_calificaciones || 'Sin calificaciones'}</p>
                </div>
            `;
            lugaresContainer.innerHTML += lugarHTML;
        });
    })
    .catch(error => console.error('Error al obtener los datos:', error));
