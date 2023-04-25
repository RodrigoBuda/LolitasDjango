import { services } from "./data.js";
const contServicio = document.getElementById("contServicio");
let queryString = location.search;
let params = new URLSearchParams(queryString);
const id = params.get("id");
const serv = services.find((d) => d._id == id);

let servicio = "";
servicio = `
<div class="card-servicio">
          <img class="tarjetas-img-servicio" src="${serv.image}" alt="" />
          <div class="card-body">
            <h3 class="card-title-servicio"><b>${serv.name}</b></h3>
            <p class="card-text-servicio"> ${serv.description} </p>
            <p class="p-price-servicio"><b> ${serv.price}</b> </p>
            <div class="cont-btns"> 
            
          <button type="button" class="boton btn-servicio"> <a>Agregar Al Carrito</a></button>
         
          <button type="button" class="boton btn-servicio"> <a>Comprar Ahora</a></button> 
          
          </div>
          </div>
          
        </div>`;

contServicio.innerHTML = servicio;
