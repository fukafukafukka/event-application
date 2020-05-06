'use strict';

{
    // 最初はどちらのFormとも閉じておく。
    const eventMakeFormId = document.getElementById('event-make-form');
    eventMakeFormId.classList.add('hidden')
    const myEventTableId = document.getElementById('my-event-table');
    myEventTableId.classList.add('hidden')

    document.getElementsByClassName('management-event-column')[0].addEventListener('click', () => {
        if(eventMakeFormId.classList.contains("hidden")){
            // クリック時非表示であったならvisibleで表示
            eventMakeFormId.classList.remove("hidden");
            eventMakeFormId.classList.add("visible");
        } else{
            // クリック時表示されていたならhiddenで非表示
            eventMakeFormId.classList.remove("visible");
            eventMakeFormId.classList.add("hidden");
        }
        if(myEventTableId.classList.contains("hidden")){
            // クリック時非表示であったならvisibleで表示
            myEventTableId.classList.remove("hidden");
            myEventTableId.classList.add("visible");
        } else{
            // クリック時表示されていたならhiddenで非表示
            myEventTableId.classList.remove("visible");
            myEventTableId.classList.add("hidden");
        }
    });
}