import { services } from "./data.js";
const contIndexServ = document.querySelector(".contIndexServ");

function TresServicios(servicios) {
  let tarjetas = "";
  for (const s of servicios.slice(0, 3)) {
    tarjetas += `
        
      <div style="background-image: linear-gradient(
      0deg,
      rgba(0, 0, 0, 0.5),
      rgba(0, 0, 0, 0.5)
    ),
    url(${s.imgIndex});
    
  background-position: center, center;
  background-size: cover;
  padding: 20px;
  margin: 20px;
  border-radius: 15px;">
            <h3 class="tit-card-index">${s.name} </h3>
            
            <p class="card-text p-description"> ${s.description} </p>
            <div class="div-puntos-susp"><h5 class="puntos-susp"> <b>...</b></h5></div>
                    <button type="button" class="boton btn-masInfo" onclick="window.location.href='/servicio?id=${s._id}'">+info</button>
                    <button type="button" class="boton btn-masInformacion" onclick="window.location.href='/servicio?id=${s._id}'">Mas Informacion</button>
            </div>

       `;
  }
  return tarjetas;
}

contIndexServ.innerHTML = TresServicios(services);
