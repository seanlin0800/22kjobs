(function () {

  angular.module('jobsApp')
    .filter('markdown', ['$window', '$sce',
      function ($window, $sce) {
        return function (input) {
          var html = $window.marked(input || '');
          return $sce.trustAsHtml(html);
        };
      }]);

}());