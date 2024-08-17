function get_random_range(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

async function get_proverbios() {
  let response = await fetch(`./proverbios.json`);
  let proverbios = await response.json();
  return proverbios.map(e => e.proverbio);
}

async function replace_quote(proverbios) {
  proverbios.then(
    data => quote.innerHTML = data[get_random_range(0, data.length)]
  )
}

proverbios = get_proverbios()
replace_quote(proverbios)

let button = document.getElementById('button')
let quote = document.getElementById('quote')

button.addEventListener('click', () => {
  replace_quote(proverbios)
})