const collapsibles = document.querySelectorAll('.rotate');

for(const collapsible of collapsibles){
    let rotation = 0;

    collapsible.style.transition = 'transform 300ms';

    collapsible.addEventListener('click', () => {
        rotation = (rotation + 180);
        collapsible.style.transform = `rotate(${rotation}deg)`
    });
}

function reload(){
    window.location.reload();
}