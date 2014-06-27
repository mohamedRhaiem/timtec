(function(angular){
    'use strict';

    angular.module('edit-portfolio-question', [
        'django',
        'directive.waiting-screen',
        'directive.alertPopup',
        'directive.contenteditable',
        'directive.codemirror',
        'timtec-models',
        'directive.fixedBar',
        'directive.markdowneditor',
        // 'directive.sortable',
        // 'filters.text',
        'youtube',
        'pdf'
        //'cgBusy'

    ]);
})(window.angular);
