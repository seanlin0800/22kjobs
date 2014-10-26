(function () {

  angular.module('jobsApp')
    .controller('JobDetailsCtrl', ['$scope', '$routeParams', 'jobService',
      function ($scope, $routeParams, jobService) {
        $scope.job = {};

        jobService.get({jobId: $routeParams.jobID}, function (value) {
            $scope.job = value.job;
        });
      }]);

}());