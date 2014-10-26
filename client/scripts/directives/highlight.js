(function () {

  angular.module('jobsApp')
    .directive('jobHighlight', [function () {
      function link(scope, element, attr) {
        element.addClass('label label-default');
        scope.$watch('text', function (value) {
          if (value > 22000) {
            element.addClass('label-success');
          }
        });
      }

      return {
        restrict: 'A',
        scope: {text: '=jobHighlight'},
        template: '{{ text | twcurrency }}',
        link: link
      };
    }]);

}());