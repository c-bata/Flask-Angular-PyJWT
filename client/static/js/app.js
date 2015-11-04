import angular from 'angular';
import { AuthenticationController } from './AuthenticationController';

let app = angular.module('ResearchRecord', [])
    .controller('AuthenticationController', AuthenticationController);

app.config(($interpolateProvider) => {
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
});
