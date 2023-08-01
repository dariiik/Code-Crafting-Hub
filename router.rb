Rails.application.routes.draw do
#looking at the index code
    root 'pages#index'

    get 'about' => 'pages#about', as: 'about'
    get 'services' => 'pages#services', as: 'services'
    get 'contact' => 'pages#contact', as: 'contact'
end
