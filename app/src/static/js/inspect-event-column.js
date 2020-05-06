'use strict';

{
    const eventTableId = document.getElementById('event-table');
    eventTableId.classList.add('hidden')
    document.getElementsByClassName('inspect-event-column')[0].addEventListener('click', () => {
        if(eventTableId.classList.contains("hidden")){
            // クリック時非表示であったならvisibleで表示
            eventTableId.classList.remove("hidden");
            eventTableId.classList.add("visible");
        }else{
            // クリック時表示されていたならhiddenで非表示
            eventTableId.classList.remove("visible");
            eventTableId.classList.add("hidden");
        }
    });
}