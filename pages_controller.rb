class PagesController < ApplicationControll:error
    def index 
        @title = 'Welcome'
        @content = 'Welcome to the homepage'
    end 
        @title = 'About'
        @content = 'Welcome to the about page'
    def about 
        @title = 'Servies'
        @content = 'Welcome to the services page'
        #for building blocks?
        @services = ['Web Design', 'Web Development', 'SEO']
    end 

    def services 
        @title = 'Welcome'
        @content = 'Contact us at...'
    end 
end
