#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Sub
%define	pnam	Assert
Summary:	Sub::Assert - Design-by-contract like pre- and postconditions, etc.
#Summary(pl):	
Name:		perl-Sub-Assert
Version:	1.22
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c3df6dba6cc6dec679fabebea6d09c39
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Sub::Assert module aims at providing design-by-contract like
subroutine pre- and postconditions. Furthermore, it allows restricting
the subroutine's calling context.

There's one big gotcha with this: It's slow. For every call to
subroutines you use assert() with, you pay for the error checking
with an extra subroutine call, some memory and some additional code
that's executed.

Fortunately, there's a workaround for mature software
which does not require you to edit a lot of your code. Instead of
use()ing Sub::Assert, you simply use Sub::Assert::Nothing and leave
the assertions intact. While you still suffer the calls to assert()
once, you won't pay the run-time penalty usually associated with
subroutine pre- and postconditions. Of course, you lose the benefits,
too, but as stated previously, this is a workaround in case you
want the verification at development time, but prefer speed in
production without refactoring your code.



# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Sub/*.pm
%dir %{perl_vendorlib}/Sub/Assert
%{perl_vendorlib}/Sub/Assert/*.pm
%{_mandir}/man3/*
