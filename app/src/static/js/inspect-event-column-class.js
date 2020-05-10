'use strict';

{
    // 最初は非表示
    const eventTableId = document.getElementById('event-table');
    eventTableId.classList.add('hidden');

    const inspectEventColumnClass = document.getElementsByClassName('inspect-event-column')[0];

    inspectEventColumnClass.addEventListener('dblclick', () => {
        if(eventTableId.classList.contains("hidden")){
            // クリック時非表示であったならvisibleで表示
            eventTableId.classList.remove("hidden");
            eventTableId.classList.add("visible");
        } else{
            // クリック時表示されていたならhiddenで非表示
            eventTableId.classList.remove("visible");
            eventTableId.classList.add("hidden");
        }
    });

    function switchByWidth(){
        if (window.matchMedia('(max-width: 567px)').matches) {
            // 画面サイズ < IPhone 5/SE 横置き幅
            inspectEventColumnClass.classList.remove('w-50');
            inspectEventColumnClass.classList.remove('width-512-and-margin-left-auto');
            inspectEventColumnClass.classList.add('w-100');
        } else if (window.matchMedia('(max-width: 1023px)').matches) {
            // 画面サイズ > IPhone 5/SE 横置き幅
            inspectEventColumnClass.classList.remove('w-100');
            inspectEventColumnClass.classList.remove('width-512-and-margin-left-auto');
            inspectEventColumnClass.classList.add('w-50');
        } else if (window.matchMedia('(min-width: 1024px)').matches) {
            // 画面サイズ > IPad 横置き幅
            inspectEventColumnClass.classList.remove('w-50');
            inspectEventColumnClass.classList.add('width-512-and-margin-left-auto');
        }
    }
    // ロードとリサイズの両方で同じ処理を付与する
    $(window).resize(switchByWidth);
    $(window).on('load',switchByWidth)

}