import createPersistedState from 'vuex-persistedstate'
import * as Cookies from 'js-cookie'
import cookie from 'cookie'

export default ({store, req, isDev}) => {
  
  createPersistedState({
      key: 'vuex',
      paths: ['auth_user_data', 'lexirus_api', 'is_authenticated'],
      storage: {
        getItem: (key) => {
          if (process.client) {
            // Try to get cookie
            const value = Cookies.get(key)
            
            if (!value) return undefined
            
            try {
              const parsed = JSON.parse(value)
              return parsed
            } catch (e) {
              return undefined
            }
          } else {
            const cookies = cookie.parse(req.headers.cookie || '')
            const value = cookies[key]
            return value ? JSON.parse(value) : undefined
          }
        },
        setItem: (key, value) => {
          
          if (!process.client) {
            return
          }
          
          try {
            const stringValue = JSON.stringify(value)
            
            // Set cookie with proper options
            Cookies.set(key, stringValue, { 
              expires: 365,
              path: '/',         
              sameSite: 'LexiRus',  
              secure: false      
            })
            
            // Wait a tick then verify
            setTimeout(() => {
              const verify = Cookies.get(key)
            }, 100)
            
          } catch (e) {
            console.error('Error setting cookie:', e)
          }
        },
        removeItem: (key) => {
          if (process.client) {
            Cookies.remove(key, { path: '/' })
          }
        }
      }
  })(store)

}