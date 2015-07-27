import Ember from 'ember';

export default Ember.Controller.extend({
    actions: {
        authenticate: function() {
            var self = this;
            var credentials = this.getProperties('identification', 'password'),
                authenticator = 'simple-auth-authenticator:jwt';
            this.get('session').authenticate(authenticator, credentials)
            .then(function(response) {
                Ember.$.ajaxSetup({
                    beforeSend: function (xhr)
                    {
                        xhr.setRequestHeader("Authorization","Bearer "+self.get('session.secure.token'));        
                    }
                });
                self.transitionToRoute('protected');
            }, function(reason) {
                self.setProperties({
                    'identification': "",
                    'password' : ""
                });
            });
        }
    }
});
