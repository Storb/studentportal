vars = {
    static: '/static/',
    static_template: '/static/angular/view/'
}

var stud = angular.module('studApp', [
    'ngRoute',
	'ngResource',
    'studentServices',
    'studControllers'
]);

stud.config(['$routeProvider',
    function($routeProvider){
        $routeProvider.when('/groups/',{
                templateUrl: vars.static_template + 'groups.html',
                controller: 'groupsListCtrl'
            }).when('/students/', {
                templateUrl: vars.static_template + 'students.html',
                controller: 'studentsCtrl'
            }).when('/groups/:id/', {
                templateUrl: vars.static_template + 'group_detail.html',
                controller: 'groupCtrl'
            });
    }]
);