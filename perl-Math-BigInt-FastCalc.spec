#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	BigInt-FastCalc
Summary:	Math::BigInt::FastCalc - some XS to support Math::BigInt
Summary(pl.UTF-8):	Math::BigInt::FastCalc - XS wspierające Math::BigInt
Name:		perl-Math-BigInt-FastCalc
Version:	0.30
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ec04fc9213e866ab6c7c323357eb57a1
URL:		http://search.cpan.org/dist/Math-BigInt-FastCalc/
BuildRequires:	perl-Math-BigInt >= 1.997
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.62
%endif
Requires:	perl-Math-BigInt >= 1.997
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a replacement library for Math::BigInt::Calc that reimplements
some of the Calc functions in XS.

%description -l pl.UTF-8
Ten moduł jest zamiennikiem Math::BigInt::Calc, będącym
reimplementacją części funkcji Calc w XS.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS README
%{perl_vendorarch}/Math/BigInt/FastCalc.pm
%dir %{perl_vendorarch}/auto/Math/BigInt/FastCalc
%attr(755,root,root) %{perl_vendorarch}/auto/Math/BigInt/FastCalc/FastCalc.so
%{_mandir}/man3/Math::BigInt::FastCalc.3pm*
