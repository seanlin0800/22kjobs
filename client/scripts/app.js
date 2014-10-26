(function () {

  angular.module('jobsApp', ['ngRoute', 'ngResource']);

  angular.module('jobsApp')
    .constant('baseUrl', 'http://127.0.0.1:5000/api/v1');

  angular.module('jobsApp')
    .config(['$routeProvider',
      function ($routeProvider) {
        $routeProvider
          .when('/', {
            templateUrl: 'views/job_list.html',
            controller: 'JobListCtrl',
          })
          .when('/jobs/:jobID', {
            templateUrl: 'views/job_details.html',
            controller: 'JobDetailsCtrl'
          })
          .when('/new', {
            templateUrl: 'views/job_form.html',
            controller: 'JobFormCtrl'
          })
          .when('/about', {
            templateUrl: 'views/about.html'
          })
          .otherwise({ redirectTo: '/'});
      }]);

}());