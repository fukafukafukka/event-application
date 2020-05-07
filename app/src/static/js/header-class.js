'use strict';

{
    const headerTag = document.getElementsByClassName('header')[0];

    function switchByWidth(){
        if (window.matchMedia('(max-width: 1023px)').matches) {
            // 画面サイズ < IPad 横置き幅
            headerTag.classList.remove('width-1024-and-margin-0-auto');
            headerTag.classList.add('w-100');
        } else if (window.matchMedia('(min-width: 1024px)').matches) {
            // 画面サイズ > IPad 横置き幅
            headerTag.classList.remove('w-100');
            headerTag.classList.add('width-1024-and-margin-0-auto');
        }
    }
    // ロードとリサイズの両方で同じ処理を付与する
    $(window).resize(switchByWidth);
    $(window).on('load',switchByWidth)
}