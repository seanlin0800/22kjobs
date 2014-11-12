(function () {
  
  var job_list = [
    {
      id: 0,
      name: 'Sweatshop Corp.',
      position: 'Principal Software Engineer',
      addr: '台北',
      min_wage: 20000,
      max_wage: 23000,
      description: 'Sweatshop is looking for a ninja programmer.\n' +
                   '- **Must** master the following skills\n' +
                   ' - C, C++, Go, Java, JavaScript, Python, Ruby\n' +
                   ' - Android, iOS, Web Frameworks\n' +
                   ' - NoSQL databases\n' +
                   '- Excellent English skills\n' +
                   '- Solid knowledge of machine learning\n' +
                   '- 10+ years of work experience',
      posted: '2014-10-24T04:44:44Z'
    }
  ];

  function findJob(jobID) {
    for (var i = 0, len = job_list.length; i < len; i++) {
      if (job_list[i].id == jobID) {
        return i;
      }
    }
    return -1;
  }

  function getJob(jobID) {
    var id = findJob(jobID);
    if (id < 0) {
      return {};
    }
    return angular.copy(job_list[id]);
  }

  function deleteJob(jobID) {
    var id = findJob(jobID);
    if (id < 0) {
      return;
    }
    job_list.splice(id, 1);
  }

  angular.module('jobsApp')
    .factory('jobService', [
      function () {
        var storageID = 'jobs_demo',
            paramDefault = 'jobId';

        return {
          get: function (params, fn) {
            if (angular.isFunction(params)) {
              fn = params;
              fn({jobs: angular.copy(job_list)});
              return;
            }
            fn({
              job: getJob(parseInt(params[paramDefault]))
            });
          },

          save: function (postData, fn) {
            postData.id = 0;
            if (job_list) {
              postData.id = job_list.slice(-1)[0].id + 1;
            }
            postData.posted = (new Date()).toISOString();
            job_list.push(postData);
            fn();
          },

          delete: function (params, fn) {
            deleteJob(parseInt(params[paramDefault]));
            fn();
          }
        }
      }]);

}());