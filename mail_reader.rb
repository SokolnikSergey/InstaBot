require 'mail'
require 'openssl'
require 'time'
require 'nokogiri'

date_request_sent = DateTime.now

login = ARGV[0]
password = ARGV[1]
puts " Try to get code from email wtih login #{login} and password #{password}"

#port(995) and protocol (pop3) can be confifured. This all was made for @mail.ru  
Mail.defaults do
  retriever_method :pop3, :address    => "pop.mail.ru",
                   :port       => 995,
                   :user_name  => "#{login}",
                   :password   => "#{password}",
                   :enable_ssl => true
end

# watiting new message from insta ( every 10 second looking for message newest then request to get message)
(0..20).each{ |el|
      Mail.last(options = {:count=>10}).each do |el|
        if el.from_addrs[0] == "security@mail.instagram.com" and  date_request_sent < el.date
          File.open("file_with_code", 'w') { |file| file.write("#{Nokogiri::HTML(el.decode_body).xpath("//p/font/text()").to_s}") }
          exit
        end
          sleep(10)
          puts "code not found"
      end
}
