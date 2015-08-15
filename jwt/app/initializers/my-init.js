export function initialize(container, application ) {
    //application.inject('initializer', 'session', 'simple-auth:session');
    //console.log(this.get('session.secure.token'));
}

export default {
  name: 'my-init',
  after: 'simple-auth',
  initialize: initialize
};
