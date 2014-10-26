(function () {

  angular.module('jobsApp')
    .controller('JobFormCtrl', ['$scope', '$location', 'jobService',
      function ($scope, $location, jobService) {
        $scope.job = {};
        $scope.preview = {
          active: false,
          text: null
        };

        function goHome() {
          $location.url('/');
        }

        $scope.preview.show = function () {
          $scope.preview.active = !$scope.preview.active;
          if ($scope.preview.active) {
            $scope.preview.text = $scope.job.description;
          }
        };

        $scope.submit = function () {
          jobService.save($scope.job, function () {
            goHome();
          });
        };

        $scope.goBack = goHome;
      }]);

}());