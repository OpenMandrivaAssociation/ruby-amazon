%define name ruby-amazon
%define version 0.9.2
%define release %mkrel 6
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




%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.9.2-6mdv2010.0
+ Revision: 433495
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.9.2-5mdv2009.0
+ Revision: 260403
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.9.2-4mdv2009.0
+ Revision: 251619
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.9.2-2mdv2008.1
+ Revision: 140753
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Apr 21 2007 Pascal Terjan <pterjan@mandriva.org> 0.9.2-2mdv2008.0
+ Revision: 16696
- Use Development/Ruby group
- Use std macros


* Sun Dec 24 2006 Stefan van der Eijk <stefan@mandriva.org> 0.9.2-2mdv2007.0
+ Revision: 102007
- fix release

  + Pascal Terjan <pterjan@mandriva.org>
    - Import ruby-amazon

* Fri Aug 25 2006 Pascal Terjan <pterjan@mandriva.org> 0.9.2-1mdv2007.0
- New release 0.9.2

* Wed Mar 02 2005 Pascal Terjan <pterjan@mandrake.org> 0.9.0-1mdk
- 0.9.0

* Thu Nov 04 2004 Pascal Terjan <pterjan@mandrake.org> 0.8.5-1mdk
- 0.8.5

* Mon Jun 28 2004 Pascal Terjan <pterjan@mandrake.org> 0.8.3-1mdk
- 0.8.3

* Mon Jun 14 2004 Pascal Terjan <pterjan@mandrake.org> 0.8.2-2mdk
- build doc

* Mon Jun 14 2004 Pascal Terjan <pterjan@mandrake.org> 0.8.2-1mdk
- first release

