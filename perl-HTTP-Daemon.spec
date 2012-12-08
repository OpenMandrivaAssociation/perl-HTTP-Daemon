%define upstream_name    HTTP-Daemon
%define upstream_version 6.00

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Base class for simple HTTP servers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/HTTP/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(HTTP::Date)
BuildRequires:	perl(HTTP::Request)
BuildRequires:	perl(HTTP::Response)
BuildRequires:	perl(HTTP::Status)
BuildRequires:	perl(IO::Socket)
BuildRequires:	perl(LWP::MediaTypes)
BuildRequires:	perl(Sys::Hostname)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Instances of the 'HTTP::Daemon' class are HTTP/1.1 servers that listen on a
socket for incoming requests. The 'HTTP::Daemon' is a subclass of
'IO::Socket::INET', so you can perform socket operations directly on it
too.

The accept() method will return when a connection from a client is
available. The returned value will be an 'HTTP::Daemon::ClientConn' object
which is another 'IO::Socket::INET' subclass. Calling the get_request()
method on this object will read data from the client and return an
'HTTP::Request' object. The ClientConn object also provide methods to send
back various responses.

This HTTP daemon does not fork(2) for you. Your application, i.e. the user
of the 'HTTP::Daemon' is responsible for forking if that is desirable. Also
note that the user is responsible for generating responses that conform to
the HTTP/1.1 protocol.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 6.0.0-3mdv2012.0
+ Revision: 765332
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 6.0.0-2
+ Revision: 763863
- rebuilt for perl-5.14.x

* Wed May 04 2011 Guillaume Rousse <guillomovitch@mandriva.org> 6.0.0-1
+ Revision: 665970
- import perl-HTTP-Daemon

