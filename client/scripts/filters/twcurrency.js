(function () {

  angular.module('jobsApp')
    .filter('twcurrency', ['numberFilter',
      function (numberFilter) {
        return function (input) {
          return '新台幣 $' + numberFilter(input, 0) + ' 元';
        };
      }]);

}());