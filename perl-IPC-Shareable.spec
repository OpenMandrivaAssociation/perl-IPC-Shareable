%define module 	IPC-Shareable

Summary:	%{module} perl module
Name: 		perl-%{module}
Version: 	0.60
Release: 	%mkrel 9
License: 	Artistic
Group:		Development/Perl
URL:		http://www.cpan.org
Source0:	%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel 
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
IPC-Shareable allows you to tie a variable to shared memory making it easy to
share the contents of that variable with other Perl processes. Scalars, arrays,
and hashes can be tied. The variable being tied may contain arbitrarily complex
data structures including references to arrays, hashes of hashes, etc.

%prep

%setup -q  -n %{module}-%{version}

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
