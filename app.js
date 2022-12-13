
function get_random_range(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

async function get_proverbios () {
    let response = await fetch('./proverbios.json')
    let data = await response.json()
    let proverbios = data
    let proverbios_array = []
    proverbios.forEach(element => {
      proverbios_array.push(element.proverbio)
    });
    return proverbios_array
}
proverbios = get_proverbios()

    
let button = document.getElementById('button')
let quote = document.getElementById('quote')

button.addEventListener('click', () => {
      let random_quote = proverbios.then(data => quote.innerHTML = data[get_random_range(0, data.length)])

      // console.log(proverbios[0])
})