%define upstream_name 	 IPC-Shareable
%define upstream_version 1.19
Name:		perl-%{upstream_name}
Version:	1.19
Release:	32

Summary:	%{upstream_name} perl module
License: 	Artistic
Group:		Development/Perl
Url:		https://github.com/stevieb9/ipc-shareable
Source0:	https://cpan.metacpan.org/authors/id/S/ST/STEVEB/IPC-Shareable-1.19.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
IPC-Shareable allows you to tie a variable to shared memory making it easy to
share the contents of that variable with other Perl processes. Scalars, arrays,
and hashes can be tied. The variable being tied may contain arbitrarily complex
data structures including references to arrays, hashes of hashes, etc.

%prep
%setup -q -n IPC-Shareable-1.19

%build
perl Makefile.PL INSTALLDIRS=vendor
make 

%check
make test || :

%install
%makeinstall_std

%files
%doc COPYING Changes META.yml
%{perl_vendorlib}/IPC
%{perl_vendorlib}/IPC/Shareable
%{_mandir}/*/*


