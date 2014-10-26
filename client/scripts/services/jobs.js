(function () {

  angular.module('jobsApp')
    .factory('jobService', ['$resource', 'baseUrl',
      function ($resource, baseUrl) {
        return $resource(
          baseUrl + '/jobs/:jobId',
          {jobId: '@jobId'}
        );
      }]);

}());