const contServicios = document.getElementById("contServicios");

const fetchData = async () => {
  const response = await fetch("../js/data.json");
  const data = await response.json();
  console.log(data);

  actualizarServicios(data);
};
fetchData();

function mostrarServicios(data) {
  let tarjetas = "";
  for (const s of data) {
    tarjetas += `
         <div class="card">
         <div class="cont-img-servicios">
          <img class="tarjetas-img" src="${s.image}" alt="" />
          </div>
          <div class="card-body">
            <div class="cont-titulo">
            <h3 class="card-title"><b>${s.name}</b></h3>
           </div>
            <p class="card-text p-description"> ${s.description} </p>
            <h5 > <b>...</b></h5>

            <button id="botonJs" type="button" class="boton btn-masDetalles" onclick="window.location.href='/servicio?id=${s._id}';">Mas Detalles</button>
          
          </div>
        </div>`;
  }
  return tarjetas;
}

function actualizarServicios(servicios) {
  contServicios.innerHTML = mostrarServicios(servicios);
}
