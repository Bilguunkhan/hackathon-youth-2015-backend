import Ember from 'ember';
import AuthenticatedRouteMixin from 'simple-auth/mixins/authenticated-route-mixin';
import ENV from '../config/environment';

export default Ember.Route.extend(AuthenticatedRouteMixin, {
    myNotification : Ember.inject.service('my-notificatoin'),
    model: function() {
        var self = this;
        return Ember.$.get(ENV['API-URL']+'/protected').then(function(response) {
            return response;
        }, function(reason) {
            return self.transitionTo('login');
        });
    },
    actions: {
        doTest: function() {
            this.get('myNotification').anotherTest();
        }
    }
});
