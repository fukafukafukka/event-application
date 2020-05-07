'use strict';

{
    // 画面幅 < IPhone 5/SE 横置き幅 の場合は画面幅一杯で表示させる。
    const applicationNameClass = document.getElementsByClassName('application-name')[0];

    function switchByWidth(){
        if (window.matchMedia('(max-width: 1023px)').matches) {
            // 画面サイズ < IPad 横置き幅
            applicationNameClass.classList.remove('w-50');
            applicationNameClass.classList.add('w-100');
        } else if (window.matchMedia('(min-width: 1024px)').matches) {
            // 画面サイズ > IPad 横置き幅
            applicationNameClass.classList.remove('w-100');
            applicationNameClass.classList.add('width-1024-and-margin-0-auto');
        }
    }
    // ロードとリサイズの両方で同じ処理を付与する
    $(window).resize(switchByWidth);
    $(window).on('load',switchByWidth)
}