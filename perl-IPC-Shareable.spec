%define upstream_name 	 IPC-Shareable
%define upstream_version 0.60

Name: 		perl-%{upstream_name}
Version: 	%perl_convert_version %{upstream_version}
Release: 	%mkrel 1

Summary:	%{upstream_name} perl module
License: 	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/IPC/%{upstream_name}-%{upstream_version}.tar.bz2

Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
IPC-Shareable allows you to tie a variable to shared memory making it easy to
share the contents of that variable with other Perl processes. Scalars, arrays,
and hashes can be tied. The variable being tied may contain arbitrarily complex
data structures including references to arrays, hashes of hashes, etc.

%prep
%setup -q  -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make 

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README MANIFEST CHANGES CREDITS 
%{perl_vendorlib}/IPC/*.pm
%{perl_vendorlib}/IPC/Shareable/*.pm
%{_mandir}/*/*
