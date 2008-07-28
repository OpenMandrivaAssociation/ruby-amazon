%define name ruby-amazon
%define version 0.9.2
%define release %mkrel 4
%define rubyver 1.8

Summary: Ruby/Amazon module for access to Amazon Web Services
Name: %name
Version: %version
Release: %release
License: GPL
Group: Development/Ruby
URL: http://www.caliban.org/ruby/
Source0: http://www.caliban.org/files/ruby/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch
BuildRequires: ruby >= %{rubyver}
Requires: ruby >= %{rubyver}

%description
Ruby/Amazon is a Ruby interface to Amazon Web Services.

%prep
%setup -q
ruby setup.rb config --prefix=$RPM_BUILD_ROOT%{_prefix}
ruby setup.rb setup

%build
rdoc -x CVS lib

%clean
rm -rf %buildroot

%install
rm -rf %buildroot
ruby setup.rb install

%files
%defattr(-,root,root)
%{ruby_sitelibdir}/amazon*
%doc COPYING INSTALL NEWS README README.rdoc TODO example doc


