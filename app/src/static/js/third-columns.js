'use strict';

{
    const myEventTableId = document.getElementById('my-event-table');
    const eventMakeFormId = document.getElementById('event-make-form');
    myEventTableId.classList.add('hidden')
    eventMakeFormId.classList.add('hidden')
    document.getElementsByClassName('third-column')[0].addEventListener('click', () => {
        if(myEventTableId.classList.contains("visible")){
            // hiddenで非表示
            myEventTableId.classList.remove("visible");
            myEventTableId.classList.add("hidden");
        }else{
            // visibleで表示
            myEventTableId.classList.remove("hidden");
            myEventTableId.classList.add("visible");
        }
        if(eventMakeFormId.classList.contains("visible")){
            // hiddenで非表示
            eventMakeFormId.classList.remove("visible");
            eventMakeFormId.classList.add("hidden");
        }else{
            // visibleで表示
            eventMakeFormId.classList.remove("hidden");
            eventMakeFormId.classList.add("visible");
        }
    });
}