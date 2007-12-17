%define module 	IPC-Shareable
%define version 0.60
%define release %mkrel 6

Summary:	%{module} perl module
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License: 	Artistic
Group:		Development/Perl
Source0:	%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel 
Url:		http://www.capn.org
Buildarch:	noarch

%description
IPC-Shareable allows you to tie a variable to shared memory 
making it easy to share the contents of that variable with 
other Perl processes.
Scalars, arrays, and hashes can be tied.  The variable being 
tied may contain arbitrarily complex data structures 
including references to arrays, hashes of hashes, etc.


%prep
%setup -q  -n %{module}-%{version}

%build

CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
make 
make test

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT PREFIX=$RPM_BUILD_ROOT%{_prefix}

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README MANIFEST CHANGES CREDITS 
%{perl_vendorlib}/IPC/*.pm
%{perl_vendorlib}/IPC/Shareable/*.pm
%{_mandir}/*/*

