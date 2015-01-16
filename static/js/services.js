var studServices = angular.module('studentServices', ['ngResource']);

studServices.factory('Students',
    function($resource){
        return $resource('/api/students/');
    }
);

studServices.factory('GroupsList',
    function($resource){
        return $resource('/api/groups/');
    }
);

studServices.factory('Group',
    function($resource){
        return $resource('/api/groups/:id/');
});