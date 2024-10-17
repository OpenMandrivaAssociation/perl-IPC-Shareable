%define upstream_name 	 IPC-Shareable
%define upstream_version 0.61

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.61
Release:	3

Summary:	%{upstream_name} perl module
License: 	Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/IPC/IPC-Shareable-0.61.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
IPC-Shareable allows you to tie a variable to shared memory making it easy to
share the contents of that variable with other Perl processes. Scalars, arrays,
and hashes can be tied. The variable being tied may contain arbitrarily complex
data structures including references to arrays, hashes of hashes, etc.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make 

%install
%makeinstall_std

%files
%doc README MANIFEST CHANGES CREDITS 
%{perl_vendorlib}/IPC/*.pm
%{perl_vendorlib}/IPC/Shareable/*.pm
%{_mandir}/*/*


%changelog
* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.600.0-1mdv2010.0
+ Revision: 402563
- rebuild using %%perl_convert_version

* Mon Sep 29 2008 Oden Eriksson <oeriksson@mandriva.com> 0.60-9mdv2009.0
+ Revision: 289647
- disable tests for now

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.60-6mdv2008.1
+ Revision: 122768
- kill re-definition of %%buildroot on Pixel's request


* Thu May 11 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.60-6mdk
- Fix Build
- use mkrel

* Wed Jun 30 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.60-5mdk
- rebuild

* Wed May 28 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.60-4mdk
- rebuild for new auto{prov,req}


