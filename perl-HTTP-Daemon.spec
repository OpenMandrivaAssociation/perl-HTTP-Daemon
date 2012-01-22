%define upstream_name    HTTP-Daemon
%define upstream_version 6.00

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:    Base class for simple HTTP servers
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/HTTP/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(HTTP::Date)
BuildRequires: perl(HTTP::Request)
BuildRequires: perl(HTTP::Response)
BuildRequires: perl(HTTP::Status)
BuildRequires: perl(IO::Socket)
BuildRequires: perl(LWP::MediaTypes)
BuildRequires: perl(Sys::Hostname)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


