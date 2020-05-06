'use strict';

{
    const secondColumnId = document.getElementById('event-table');
    secondColumnId.classList.add('hidden')
    document.getElementsByClassName('second-column')[0].addEventListener('click', () => {
        if(secondColumnId.classList.contains("visible")){
            // hiddenで非表示
            secondColumnId.classList.remove("visible");
            secondColumnId.classList.add("hidden");
        }else{
            // visibleで表示
            secondColumnId.classList.remove("hidden");
            secondColumnId.classList.add("visible");
        }
    });
}