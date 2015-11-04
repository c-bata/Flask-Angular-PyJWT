class AuthenticationController {
    constructor($http){
        this.$http = $http;
        this.users = [];
        this.getUsers();
    }

    getUsers() {
        this.users = this.$http.get('/api/users')
            .success((data) => {
                this.users = data['users'];
            });
    }

    createUser() {
        this.$http.post('/api/users', {'name': this.username, 'password': this.password})
            .success((data, status, headers, config) => {
                console.log(data);
                this.users.push(data);
            })
            .error((data, status, headers, config) => {
                console.log(data);
            });

        this.username = '';
        this.password = '';
    };
}
export { AuthenticationController }
