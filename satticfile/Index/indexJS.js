
function load () {

    loadHTML = document.getElementById ('loadingID')
    LoadContainer = document.getElementById ('LoadContainer')

    loadHTML.classList.add ('redirectload')
    LoadContainer.classList.add ('cancel')

}

setTimeout (load, 3000)