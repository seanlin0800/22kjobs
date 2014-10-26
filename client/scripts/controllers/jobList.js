(function () {

  var search_fields = ['name', 'position', 'description', 'addr'];

  angular.module('jobsApp')
    .controller('JobListCtrl', ['$scope', 'jobService',
      function ($scope, jobService) {

        function init() {
          $scope.jobs = [];
          $scope.query = '';
          jobService.get(function (value) {
            $scope.jobs = value.jobs;
          });
        }

        $scope.deleteJob = function (job) {
          jobService.delete({jobId: job.id}, function () {
            $scope.jobs.splice($scope.jobs.indexOf(job), 1);
          });
        };

        $scope.search = function (row) {
          return search_fields.some(function (element) {
            if (row[element].indexOf($scope.query) > -1) {
              return true;
            }
            return false;
          });
        };

        init();
      }]);

}());