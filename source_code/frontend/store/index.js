export const state = () => ({

    auth_user_data: null,
    is_authenticated: false,

})

export const mutations = {

    // Store authentication data
    store_auth_data(state, payload) {
        
        state.auth_user_data = { ...payload, is_authenticated: true }
    },

    // Clear authentication data
    clear_auth_data(state) {
        state.auth_user_data = null
    },

}
