'use strict';

var studControllers = angular.module('studControllers', []);

studControllers.controller('studentsCtrl',
    function($scope, Students){
        $scope.students = Students.query();
    }
);
studControllers.controller('groupsListCtrl',
    function($scope, GroupsList, $http, $modalInstance, group){
        $scope.groupslist = GroupsList.query();
    }
);
studControllers.controller('groupCtrl',
    function($scope, Group, $modalInstance, group){
        $scope.group = Group.query({id: group.id});
    }
);

//yovaControllers.controller('feedsCtrl', function($scope, $http){
//  $http({method: 'GET', url: '/api/v1/feeds.json'}).
//    success(function(data, status, headers, config) {
//      console.log(data);
//      console.log(data.feeds);
//      $scope.feedLimit = 7;
//      $scope.showMore = function() {
//        $scope.feedLimit += 5;
//      }
//      $scope.feeds = data.feeds;
//    }).
//    error(function(data, status, headers, config) {
//      // Called asynchronously if an error occurs
//      console.log("Failed to retrieve user messages");
//    });
//
//});