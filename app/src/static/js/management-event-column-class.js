'use strict';

{
    // 最初はどちらのFormとも閉じておく。
    const eventMakeFormId = document.getElementById('event-make-form');
    eventMakeFormId.classList.add('hidden')
    const myEventTableId = document.getElementById('my-event-table');
    myEventTableId.classList.add('hidden')

    const managementEventColumnClass = document.getElementsByClassName('management-event-column')[0];

    managementEventColumnClass.addEventListener('click', () => {
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

    function switchByWidth(){
        if (window.matchMedia('(max-width: 567px)').matches) {
            // 画面サイズ < IPhone 5/SE 横置き幅
            managementEventColumnClass.classList.remove('w-50');
            managementEventColumnClass.classList.remove('width-512-and-margin-right-auto');
            managementEventColumnClass.classList.add('w-100');
        } else if (window.matchMedia('(max-width: 1023px)').matches) {
            // 画面サイズ > IPhone 5/SE 横置き幅
            managementEventColumnClass.classList.remove('w-100');
            managementEventColumnClass.classList.remove('width-512-and-margin-right-auto');
            managementEventColumnClass.classList.add('w-50');
        } else if (window.matchMedia('(min-width: 1024px)').matches) {
            // 画面サイズ > IPad 横置き幅
            managementEventColumnClass.classList.remove('w-50');
            managementEventColumnClass.classList.add('width-512-and-margin-right-auto');
        }
    }
    // ロードとリサイズの両方で同じ処理を付与する
    $(window).resize(switchByWidth);
    $(window).on('load',switchByWidth)
}