const contServicio = document.getElementById("contServicio");
const queryString = window.location.search;
const params = new URLSearchParams(queryString);
const id = params.get("id");

const fetchData = async () => {
  try {
    const response = await fetch("../js/data.json");
    const data = await response.json();
    console.log(data);

    const serv = data.find((d) => d._id == id);
    mostrarServicio(serv);
  } catch (error) {
    console.error("Error al obtener los datos:", error);
  }
};
fetchData();

function mostrarServicio(serv) {
  const servicio = `
      <div class="card-servicio">
        <img class="tarjetas-img-servicio" src="${serv.image}" alt="" />
        <div class="card-body">
          <h3 class="card-title-servicio"><b>${serv.name}</b></h3>
          <p class="card-text-servicio">${serv.description}</p>
          <p class="p-price-servicio"><b>${serv.price}</b></p>
          <div class="cont-btns">
            <button type="button" class="boton btn-servicio"><a>Agregar Al Carrito</a></button>
            <button type="button" class="boton btn-servicio"><a>Comprar Ahora</a></button>
          </div>
        </div>
      </div>`;

  contServicio.innerHTML = servicio;
}
